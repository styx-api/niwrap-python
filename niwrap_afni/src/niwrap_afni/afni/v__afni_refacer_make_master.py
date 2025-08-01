# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__AFNI_REFACER_MAKE_MASTER_METADATA = Metadata(
    id="754d45612350ae723d8b3264a150b211e0e4c0e8.boutiques",
    name="@afni_refacer_make_master",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VAfniRefacerMakeMasterParameters = typing.TypedDict('VAfniRefacerMakeMasterParameters', {
    "__STYXTYPE__": typing.Literal["@afni_refacer_make_master"],
    "input_datasets": list[InputPathType],
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
        "@afni_refacer_make_master": v__afni_refacer_make_master_cargs,
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
        "@afni_refacer_make_master": v__afni_refacer_make_master_outputs,
    }.get(t)


class VAfniRefacerMakeMasterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_refacer_make_master(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_shell_dataset: OutputPathType
    """Output dataset containing the average 'face' (non-brain tissue)."""


def v__afni_refacer_make_master_params(
    input_datasets: list[InputPathType],
) -> VAfniRefacerMakeMasterParameters:
    """
    Build parameters.
    
    Args:
        input_datasets: List of T1-weighted datasets that have NOT been\
            skull-stripped, defaced, or refaced.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@afni_refacer_make_master",
        "input_datasets": input_datasets,
    }
    return params


def v__afni_refacer_make_master_cargs(
    params: VAfniRefacerMakeMasterParameters,
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
    cargs.append("@afni_refacer_make_master")
    cargs.extend([execution.input_file(f) for f in params.get("input_datasets")])
    return cargs


def v__afni_refacer_make_master_outputs(
    params: VAfniRefacerMakeMasterParameters,
    execution: Execution,
) -> VAfniRefacerMakeMasterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAfniRefacerMakeMasterOutputs(
        root=execution.output_file("."),
        output_shell_dataset=execution.output_file("afni_refacer_shell.nii.gz"),
    )
    return ret


def v__afni_refacer_make_master_execute(
    params: VAfniRefacerMakeMasterParameters,
    execution: Execution,
) -> VAfniRefacerMakeMasterOutputs:
    """
    This script makes a new mask/shell dataset for use with @afni_refacer_run by
    averaging 'faces' (non-brain tissue) from input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAfniRefacerMakeMasterOutputs`).
    """
    params = execution.params(params)
    cargs = v__afni_refacer_make_master_cargs(params, execution)
    ret = v__afni_refacer_make_master_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__afni_refacer_make_master(
    input_datasets: list[InputPathType],
    runner: Runner | None = None,
) -> VAfniRefacerMakeMasterOutputs:
    """
    This script makes a new mask/shell dataset for use with @afni_refacer_run by
    averaging 'faces' (non-brain tissue) from input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_datasets: List of T1-weighted datasets that have NOT been\
            skull-stripped, defaced, or refaced.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniRefacerMakeMasterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_REFACER_MAKE_MASTER_METADATA)
    params = v__afni_refacer_make_master_params(
        input_datasets=input_datasets,
    )
    return v__afni_refacer_make_master_execute(params, execution)


__all__ = [
    "VAfniRefacerMakeMasterOutputs",
    "VAfniRefacerMakeMasterParameters",
    "V__AFNI_REFACER_MAKE_MASTER_METADATA",
    "v__afni_refacer_make_master",
    "v__afni_refacer_make_master_params",
]
