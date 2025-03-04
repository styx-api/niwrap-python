# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_GCA_AMBIGUOUS_METADATA = Metadata(
    id="cdd8244223ec0fbd63686859a42564580f8c6dee.boutiques",
    name="mri_gca_ambiguous",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriGcaAmbiguousParameters = typing.TypedDict('MriGcaAmbiguousParameters', {
    "__STYX_TYPE__": typing.Literal["mri_gca_ambiguous"],
    "gca_file": InputPathType,
    "output_volume": str,
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
        "mri_gca_ambiguous": mri_gca_ambiguous_cargs,
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
        "mri_gca_ambiguous": mri_gca_ambiguous_outputs,
    }.get(t)


class MriGcaAmbiguousOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gca_ambiguous(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Resulting MR image file with computed ambiguity measure"""


def mri_gca_ambiguous_params(
    gca_file: InputPathType,
    output_volume: str,
) -> MriGcaAmbiguousParameters:
    """
    Build parameters.
    
    Args:
        gca_file: The input GCA file.
        output_volume: The output MR image file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_gca_ambiguous",
        "gca_file": gca_file,
        "output_volume": output_volume,
    }
    return params


def mri_gca_ambiguous_cargs(
    params: MriGcaAmbiguousParameters,
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
    cargs.append("mri_gca_ambiguous")
    cargs.append(execution.input_file(params.get("gca_file")))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_gca_ambiguous_outputs(
    params: MriGcaAmbiguousParameters,
    execution: Execution,
) -> MriGcaAmbiguousOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriGcaAmbiguousOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_gca_ambiguous_execute(
    params: MriGcaAmbiguousParameters,
    execution: Execution,
) -> MriGcaAmbiguousOutputs:
    """
    This program computes an ambiguity measure across a GCA and outputs an MR image
    of it.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriGcaAmbiguousOutputs`).
    """
    params = execution.params(params)
    cargs = mri_gca_ambiguous_cargs(params, execution)
    ret = mri_gca_ambiguous_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_gca_ambiguous(
    gca_file: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriGcaAmbiguousOutputs:
    """
    This program computes an ambiguity measure across a GCA and outputs an MR image
    of it.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gca_file: The input GCA file.
        output_volume: The output MR image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGcaAmbiguousOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GCA_AMBIGUOUS_METADATA)
    params = mri_gca_ambiguous_params(
        gca_file=gca_file,
        output_volume=output_volume,
    )
    return mri_gca_ambiguous_execute(params, execution)


__all__ = [
    "MRI_GCA_AMBIGUOUS_METADATA",
    "MriGcaAmbiguousOutputs",
    "MriGcaAmbiguousParameters",
    "mri_gca_ambiguous",
    "mri_gca_ambiguous_params",
]
