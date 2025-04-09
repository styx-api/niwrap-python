# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TEST_RECON_ALL_CSH_METADATA = Metadata(
    id="ad546a46131f123c3acbd5d9a9ec493899bfd06e.boutiques",
    name="test_recon-all.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TestReconAllCshParameters = typing.TypedDict('TestReconAllCshParameters', {
    "__STYX_TYPE__": typing.Literal["test_recon-all.csh"],
    "reference_subj_source_dir": typing.NotRequired[str | None],
    "reference_subjid": typing.NotRequired[str | None],
    "test_subject_dest_dir": typing.NotRequired[str | None],
    "test_subjid": typing.NotRequired[str | None],
    "freesurfer_home": typing.NotRequired[str | None],
    "norecon": bool,
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
        "test_recon-all.csh": test_recon_all_csh_cargs,
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
        "test_recon-all.csh": test_recon_all_csh_outputs,
    }.get(t)


class TestReconAllCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `test_recon_all_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    recon_all_output: OutputPathType
    """Output from the recon-all utility."""
    mri_diff_output: OutputPathType
    """Output from the mri_diff utility."""
    mri_compute_seg_overlap_output: OutputPathType
    """Output from the mri_compute_seg_overlap utility."""
    mris_diff_output: OutputPathType
    """Output from the mris_diff utility."""
    mri_surf2surf_output: OutputPathType
    """Output from the mri_surf2surf utility."""
    mris_compute_parc_overlap_output: OutputPathType
    """Output from the mris_compute_parc_overlap utility."""
    diff_output: OutputPathType
    """Output from the diff utility."""
    asegstatsdiff_output: OutputPathType
    """Output from the asegstatsdiff utility."""
    aparcstatsdiff_output: OutputPathType
    """Output from the aparcstatsdiff utility."""


def test_recon_all_csh_params(
    reference_subj_source_dir: str | None = "/space/freesurfer/subjects/test/weekly_test/subjects/x86_64",
    reference_subjid: str | None = "bert",
    test_subject_dest_dir: str | None = "/tmp",
    test_subjid: str | None = "bert",
    freesurfer_home: str | None = "/usr/local/freesurfer/stable",
    norecon: bool = False,
) -> TestReconAllCshParameters:
    """
    Build parameters.
    
    Args:
        reference_subj_source_dir: Directory of the reference subject source.
        reference_subjid: ID of the reference subject.
        test_subject_dest_dir: Directory for the test subject destination.
        test_subjid: ID of the test subject.
        freesurfer_home: Path to the FreeSurfer installation directory.
        norecon: Flag to indicate that recon-all should not be run.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "test_recon-all.csh",
        "norecon": norecon,
    }
    if reference_subj_source_dir is not None:
        params["reference_subj_source_dir"] = reference_subj_source_dir
    if reference_subjid is not None:
        params["reference_subjid"] = reference_subjid
    if test_subject_dest_dir is not None:
        params["test_subject_dest_dir"] = test_subject_dest_dir
    if test_subjid is not None:
        params["test_subjid"] = test_subjid
    if freesurfer_home is not None:
        params["freesurfer_home"] = freesurfer_home
    return params


def test_recon_all_csh_cargs(
    params: TestReconAllCshParameters,
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
    cargs.append("test_recon-all.csh")
    if params.get("reference_subj_source_dir") is not None:
        cargs.extend([
            "-rsd",
            params.get("reference_subj_source_dir")
        ])
    if params.get("reference_subjid") is not None:
        cargs.extend([
            "-rs",
            params.get("reference_subjid")
        ])
    if params.get("test_subject_dest_dir") is not None:
        cargs.extend([
            "-tsd",
            params.get("test_subject_dest_dir")
        ])
    if params.get("test_subjid") is not None:
        cargs.extend([
            "-ts",
            params.get("test_subjid")
        ])
    if params.get("freesurfer_home") is not None:
        cargs.extend([
            "-fshome",
            params.get("freesurfer_home")
        ])
    if params.get("norecon"):
        cargs.append("-norecon")
    return cargs


def test_recon_all_csh_outputs(
    params: TestReconAllCshParameters,
    execution: Execution,
) -> TestReconAllCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TestReconAllCshOutputs(
        root=execution.output_file("."),
        recon_all_output=execution.output_file("recon_all_output.txt"),
        mri_diff_output=execution.output_file("mri_diff_output.txt"),
        mri_compute_seg_overlap_output=execution.output_file("mri_compute_seg_overlap_output.txt"),
        mris_diff_output=execution.output_file("mris_diff_output.txt"),
        mri_surf2surf_output=execution.output_file("mri_surf2surf_output.txt"),
        mris_compute_parc_overlap_output=execution.output_file("mris_compute_parc_overlap_output.txt"),
        diff_output=execution.output_file("diff_output.txt"),
        asegstatsdiff_output=execution.output_file("asegstatsdiff_output.txt"),
        aparcstatsdiff_output=execution.output_file("aparcstatsdiff_output.txt"),
    )
    return ret


def test_recon_all_csh_execute(
    params: TestReconAllCshParameters,
    execution: Execution,
) -> TestReconAllCshOutputs:
    """
    Script for testing recon-all and other utilities with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TestReconAllCshOutputs`).
    """
    params = execution.params(params)
    cargs = test_recon_all_csh_cargs(params, execution)
    ret = test_recon_all_csh_outputs(params, execution)
    execution.run(cargs)
    return ret


def test_recon_all_csh(
    reference_subj_source_dir: str | None = "/space/freesurfer/subjects/test/weekly_test/subjects/x86_64",
    reference_subjid: str | None = "bert",
    test_subject_dest_dir: str | None = "/tmp",
    test_subjid: str | None = "bert",
    freesurfer_home: str | None = "/usr/local/freesurfer/stable",
    norecon: bool = False,
    runner: Runner | None = None,
) -> TestReconAllCshOutputs:
    """
    Script for testing recon-all and other utilities with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        reference_subj_source_dir: Directory of the reference subject source.
        reference_subjid: ID of the reference subject.
        test_subject_dest_dir: Directory for the test subject destination.
        test_subjid: ID of the test subject.
        freesurfer_home: Path to the FreeSurfer installation directory.
        norecon: Flag to indicate that recon-all should not be run.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TestReconAllCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEST_RECON_ALL_CSH_METADATA)
    params = test_recon_all_csh_params(
        reference_subj_source_dir=reference_subj_source_dir,
        reference_subjid=reference_subjid,
        test_subject_dest_dir=test_subject_dest_dir,
        test_subjid=test_subjid,
        freesurfer_home=freesurfer_home,
        norecon=norecon,
    )
    return test_recon_all_csh_execute(params, execution)


__all__ = [
    "TEST_RECON_ALL_CSH_METADATA",
    "TestReconAllCshOutputs",
    "TestReconAllCshParameters",
    "test_recon_all_csh",
    "test_recon_all_csh_params",
]
