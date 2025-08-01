# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_DCT_ALIGN_BINARY_METADATA = Metadata(
    id="e05c8e053f59a6f74a1ef04223f889b8dedd61aa.boutiques",
    name="mri_dct_align_binary",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriDctAlignBinaryParameters = typing.TypedDict('MriDctAlignBinaryParameters', {
    "__STYXTYPE__": typing.Literal["mri_dct_align_binary"],
    "source_image": InputPathType,
    "destination_image": InputPathType,
    "output_transformation": str,
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
        "mri_dct_align_binary": mri_dct_align_binary_cargs,
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
        "mri_dct_align_binary": mri_dct_align_binary_outputs,
    }.get(t)


class MriDctAlignBinaryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_dct_align_binary(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transformation_file: OutputPathType
    """The resulting transformation from the alignment"""


def mri_dct_align_binary_params(
    source_image: InputPathType,
    destination_image: InputPathType,
    output_transformation: str,
) -> MriDctAlignBinaryParameters:
    """
    Build parameters.
    
    Args:
        source_image: Source image for alignment.
        destination_image: Destination image for alignment.
        output_transformation: Output transformation file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_dct_align_binary",
        "source_image": source_image,
        "destination_image": destination_image,
        "output_transformation": output_transformation,
    }
    return params


def mri_dct_align_binary_cargs(
    params: MriDctAlignBinaryParameters,
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
    cargs.append("mri_dct_align_binary")
    cargs.append(execution.input_file(params.get("source_image")))
    cargs.append(execution.input_file(params.get("destination_image")))
    cargs.append(params.get("output_transformation"))
    return cargs


def mri_dct_align_binary_outputs(
    params: MriDctAlignBinaryParameters,
    execution: Execution,
) -> MriDctAlignBinaryOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriDctAlignBinaryOutputs(
        root=execution.output_file("."),
        output_transformation_file=execution.output_file(params.get("output_transformation")),
    )
    return ret


def mri_dct_align_binary_execute(
    params: MriDctAlignBinaryParameters,
    execution: Execution,
) -> MriDctAlignBinaryOutputs:
    """
    A binary tool for aligning MRI images using DCT.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriDctAlignBinaryOutputs`).
    """
    params = execution.params(params)
    cargs = mri_dct_align_binary_cargs(params, execution)
    ret = mri_dct_align_binary_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_dct_align_binary(
    source_image: InputPathType,
    destination_image: InputPathType,
    output_transformation: str,
    runner: Runner | None = None,
) -> MriDctAlignBinaryOutputs:
    """
    A binary tool for aligning MRI images using DCT.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_image: Source image for alignment.
        destination_image: Destination image for alignment.
        output_transformation: Output transformation file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriDctAlignBinaryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_DCT_ALIGN_BINARY_METADATA)
    params = mri_dct_align_binary_params(
        source_image=source_image,
        destination_image=destination_image,
        output_transformation=output_transformation,
    )
    return mri_dct_align_binary_execute(params, execution)


__all__ = [
    "MRI_DCT_ALIGN_BINARY_METADATA",
    "MriDctAlignBinaryOutputs",
    "MriDctAlignBinaryParameters",
    "mri_dct_align_binary",
    "mri_dct_align_binary_params",
]
