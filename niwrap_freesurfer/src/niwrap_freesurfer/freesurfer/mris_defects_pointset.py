# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_DEFECTS_POINTSET_METADATA = Metadata(
    id="9eb7afe68027662a0838780e0a4bc4bbc0ca9d5f.boutiques",
    name="mris_defects_pointset",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisDefectsPointsetParameters = typing.TypedDict('MrisDefectsPointsetParameters', {
    "__STYX_TYPE__": typing.Literal["mris_defects_pointset"],
    "surface": InputPathType,
    "defects": InputPathType,
    "out": str,
    "label": typing.NotRequired[InputPathType | None],
    "control": bool,
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
        "mris_defects_pointset": mris_defects_pointset_cargs,
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
        "mris_defects_pointset": mris_defects_pointset_outputs,
    }.get(t)


class MrisDefectsPointsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_defects_pointset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    pointset_output: OutputPathType
    """Output pointset file containing locations of topological defects"""


def mris_defects_pointset_params(
    surface: InputPathType,
    defects: InputPathType,
    out: str,
    label: InputPathType | None = None,
    control: bool = False,
) -> MrisDefectsPointsetParameters:
    """
    Build parameters.
    
    Args:
        surface: Input surface.
        defects: Input defect label (must match the surface dimensions).
        out: Output pointset file (json).
        label: Restrict pointset to this label (must be in input surface space).
        control: Save output in old control point format (v6 compatible).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_defects_pointset",
        "surface": surface,
        "defects": defects,
        "out": out,
        "control": control,
    }
    if label is not None:
        params["label"] = label
    return params


def mris_defects_pointset_cargs(
    params: MrisDefectsPointsetParameters,
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
    cargs.append("mris_defects_pointset")
    cargs.extend([
        "--surf",
        execution.input_file(params.get("surface"))
    ])
    cargs.extend([
        "--defects",
        execution.input_file(params.get("defects"))
    ])
    cargs.extend([
        "--out",
        params.get("out")
    ])
    if params.get("label") is not None:
        cargs.extend([
            "--label",
            execution.input_file(params.get("label"))
        ])
    if params.get("control"):
        cargs.append("--control")
    return cargs


def mris_defects_pointset_outputs(
    params: MrisDefectsPointsetParameters,
    execution: Execution,
) -> MrisDefectsPointsetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisDefectsPointsetOutputs(
        root=execution.output_file("."),
        pointset_output=execution.output_file(params.get("out")),
    )
    return ret


def mris_defects_pointset_execute(
    params: MrisDefectsPointsetParameters,
    execution: Execution,
) -> MrisDefectsPointsetOutputs:
    """
    Produces a pointset file containing the locations of each topological defect in
    a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisDefectsPointsetOutputs`).
    """
    params = execution.params(params)
    cargs = mris_defects_pointset_cargs(params, execution)
    ret = mris_defects_pointset_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_defects_pointset(
    surface: InputPathType,
    defects: InputPathType,
    out: str,
    label: InputPathType | None = None,
    control: bool = False,
    runner: Runner | None = None,
) -> MrisDefectsPointsetOutputs:
    """
    Produces a pointset file containing the locations of each topological defect in
    a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Input surface.
        defects: Input defect label (must match the surface dimensions).
        out: Output pointset file (json).
        label: Restrict pointset to this label (must be in input surface space).
        control: Save output in old control point format (v6 compatible).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisDefectsPointsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_DEFECTS_POINTSET_METADATA)
    params = mris_defects_pointset_params(
        surface=surface,
        defects=defects,
        out=out,
        label=label,
        control=control,
    )
    return mris_defects_pointset_execute(params, execution)


__all__ = [
    "MRIS_DEFECTS_POINTSET_METADATA",
    "MrisDefectsPointsetOutputs",
    "MrisDefectsPointsetParameters",
    "mris_defects_pointset",
    "mris_defects_pointset_params",
]
