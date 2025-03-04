# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_CORTEX_LABEL_METADATA = Metadata(
    id="f144e3d1e0fdf022a6e2282c867ba8f46fafc1cb.boutiques",
    name="make_cortex_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MakeCortexLabelParameters = typing.TypedDict('MakeCortexLabelParameters', {
    "__STYX_TYPE__": typing.Literal["make_cortex_label"],
    "subject": str,
    "hemi": typing.NotRequired[str | None],
    "use_a2009s": bool,
    "output_name": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "make_cortex_label": make_cortex_label_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "make_cortex_label": make_cortex_label_outputs,
    }.get(t)


class MakeCortexLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_cortex_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType | None
    """The output cortex label file."""


def make_cortex_label_params(
    subject: str,
    hemi: str | None = None,
    use_a2009s: bool = False,
    output_name: str | None = "cortex",
) -> MakeCortexLabelParameters:
    """
    Build parameters.
    
    Args:
        subject: The subject for which the cortex label is to be created.
        hemi: The hemisphere(s) on which to operate. Default is both\
            hemispheres.
        use_a2009s: Use aparc.a2009 instead of aparc.
        output_name: Output name. The output will be ?h.outname.label. Default\
            is 'cortex'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make_cortex_label",
        "subject": subject,
        "use_a2009s": use_a2009s,
    }
    if hemi is not None:
        params["hemi"] = hemi
    if output_name is not None:
        params["output_name"] = output_name
    return params


def make_cortex_label_cargs(
    params: MakeCortexLabelParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("make_cortex_label")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--h",
            params.get("hemi")
        ])
    if params.get("use_a2009s"):
        cargs.append("--a2009s")
    if params.get("output_name") is not None:
        cargs.extend([
            "--o",
            params.get("output_name")
        ])
    return cargs


def make_cortex_label_outputs(
    params: MakeCortexLabelParameters,
    execution: Execution,
) -> MakeCortexLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeCortexLabelOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file("?h." + params.get("output_name") + ".label") if (params.get("output_name") is not None) else None,
    )
    return ret


def make_cortex_label_execute(
    params: MakeCortexLabelParameters,
    execution: Execution,
) -> MakeCortexLabelOutputs:
    """
    A tool to create cortical labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeCortexLabelOutputs`).
    """
    params = execution.params(params)
    cargs = make_cortex_label_cargs(params, execution)
    ret = make_cortex_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_cortex_label(
    subject: str,
    hemi: str | None = None,
    use_a2009s: bool = False,
    output_name: str | None = "cortex",
    runner: Runner | None = None,
) -> MakeCortexLabelOutputs:
    """
    A tool to create cortical labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject for which the cortex label is to be created.
        hemi: The hemisphere(s) on which to operate. Default is both\
            hemispheres.
        use_a2009s: Use aparc.a2009 instead of aparc.
        output_name: Output name. The output will be ?h.outname.label. Default\
            is 'cortex'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeCortexLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_CORTEX_LABEL_METADATA)
    params = make_cortex_label_params(
        subject=subject,
        hemi=hemi,
        use_a2009s=use_a2009s,
        output_name=output_name,
    )
    return make_cortex_label_execute(params, execution)


__all__ = [
    "MAKE_CORTEX_LABEL_METADATA",
    "MakeCortexLabelOutputs",
    "MakeCortexLabelParameters",
    "make_cortex_label",
    "make_cortex_label_params",
]
